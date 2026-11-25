const PAQUETS = __PAQUETS__;
const PCOL = ["#E8456B","#1E6FD9","#22A06B","#A855F7"];
const N = 24;
const CAMB = {0:0, 4:1, 8:2, 12:3, 16:4, 20:5};   // position -> index de catégorie

const $ = s => document.querySelector(s);
let G = {players:[], turn:0, phase:"roll", q:null, ci:0, used:new Set(), rolled:false, pak:null};

/* ---------- choix du paquet ---------- */
function renderPacks(){
  const box = $("#pakList"); box.innerHTML = "";
  PAQUETS.forEach(p => {
    const b = document.createElement("button");
    b.className = "play";
    b.style.cssText = "margin:0;background:#fff;color:var(--ink);border:3px solid var(--ink);box-shadow:3px 3px 0 var(--ink);text-align:left;padding:13px 15px;font-size:14.5px";
    b.innerHTML = '<span style="font-size:19px;margin-right:8px">'+p.em+'</span><b>'+p.nom+'</b>'+
      '<span style="display:block;font-size:11.5px;font-weight:600;color:var(--ink2);margin-top:3px">'+p.desc+' · '+p.q.length+' questions</span>';
    b.onclick = () => startGame(p);
    box.appendChild(b);
  });
  const nm = $("#names"); nm.innerHTML = "";
  for(let i=0;i<nbPlayers;i++){
    const inp=document.createElement("input"); inp.placeholder="Joueur "+(i+1); inp.maxLength=12; nm.appendChild(inp);
  }
}
let nbPlayers = 2;
function renderSetup(){
  const p=$("#pcount"); p.innerHTML="";
  [1,2,3,4].forEach(n=>{const b=document.createElement("button");b.textContent=n;b.className=n===nbPlayers?"on":"";
    b.onclick=()=>{nbPlayers=n;renderSetup();};p.appendChild(b);});
  renderPacks();
}

function startGame(pak){
  const ins=[...document.querySelectorAll("#names input")];
  G.players=ins.map((x,i)=>({name:x.value.trim()||"Joueur "+(i+1),parts:[],pos:0,color:PCOL[i]}));
  G.turn=0; G.phase="roll"; G.q=null; G.used=new Set(); G.pak=pak;
  show("v-game"); draw(); renderSide(); $("#qzone").innerHTML="";
}

/* ---------- helpers ---------- */
function show(id){document.querySelectorAll(".view").forEach(v=>v.classList.toggle("on",v.id===id));window.scrollTo({top:0,behavior:"instant"});}
function catIndexAt(pos){ return (pos in CAMB) ? CAMB[pos] : (pos % 6); }
function isCamb(pos){ return pos in CAMB; }
function pickQ(ci){
  const cat = G.pak.cats[ci].id;
  const SRC = G.pak.q;
  let pool = SRC.filter(q => q.c === cat && !G.used.has(q));
  if(pool.length === 0){ SRC.filter(q => q.c === cat).forEach(q => G.used.delete(q)); pool = SRC.filter(q => q.c === cat); }
  if(pool.length === 0) pool = SRC;
  const q = pool[Math.floor(Math.random()*pool.length)];
  G.used.add(q); return q;
}
function pol(cx,cy,r,a){const x=(a-90)*Math.PI/180;return [cx+r*Math.cos(x),cy+r*Math.sin(x)];}

/* ---------- plateau ---------- */
function draw(){
  const svg=$("#board"); let s="";
  s+=`<circle cx="170" cy="170" r="152" fill="#FFFDF6" stroke="#1B2440" stroke-width="3"/>`;
  for(let i=0;i<N;i++){
    const a=i*(360/N), [x,y]=pol(170,170,128,a);
    const cam=isCamb(i), c=G.pak.cats[catIndexAt(i)].c;
    s+=`<circle cx="${x}" cy="${y}" r="${cam?15:10}" fill="${c}" stroke="#1B2440" stroke-width="${cam?3:2}"/>`;
    if(cam) s+=`<circle cx="${x}" cy="${y}" r="6" fill="#FFFDF6" stroke="#1B2440" stroke-width="1.5"/>`;
  }
  G.players.forEach((p,pi)=>{
    const a=p.pos*(360/N), [x,y]=pol(170,170,128,a);
    const off=(pi-(G.players.length-1)/2)*5.5;
    s+=`<circle cx="${x+off}" cy="${y+off}" r="7.5" fill="${p.color}" stroke="#fff" stroke-width="2.5"/>`;
    s+=`<text x="${x+off}" y="${y+off+3.5}" text-anchor="middle" font-size="8" font-weight="800" fill="#fff">${p.name.slice(0,1).toUpperCase()}</text>`;
  });
  svg.innerHTML=s;
}
function renderSide(){
  const p=G.players[G.turn];
  $("#pdot").style.background=p.color;
  $("#who").textContent="Au tour de "+p.name;
  $("#sub").textContent=p.parts.length+"/6 camemberts · case "+(p.pos+1)+"/"+N+(G.pak?" · "+G.pak.nom:"");
  const pl=$("#plist"); pl.innerHTML="";
  G.players.forEach((x,i)=>{
    const d=document.createElement("div"); d.className="pl"+(i===G.turn?" act":"");
    d.innerHTML='<span class="dot" style="width:9px;height:9px;background:'+x.color+';border-width:1.5px"></span>'+x.name+' '+x.parts.length+'/6';
    pl.appendChild(d);
  });
  $("#roll").disabled = G.phase!=="roll";
  $("#roll").textContent = G.phase==="roll" ? "Lancer le dé 🎲" : "Question en cours…";
}

/* ---------- dé ---------- */
$("#roll").onclick=()=>{
  if(G.phase!=="roll") return;
  const dice=$("#dice"); dice.classList.add("roll"); $("#roll").disabled=true;
  const spin=setInterval(()=>{dice.textContent=1+Math.floor(Math.random()*6);},70);
  setTimeout(()=>{
    clearInterval(spin); dice.classList.remove("roll");
    const n=1+Math.floor(Math.random()*6); dice.textContent=n;
    const p=G.players[G.turn];
    p.pos=(p.pos+n)%N; draw(); renderSide();
    setTimeout(()=>askQuestion(p.pos),260);
  },720);
};

/* ---------- question ---------- */
function askQuestion(pos){
  const ci=catIndexAt(pos), c=G.pak.cats[ci];
  G.ci=ci; G.q=pickQ(ci); G.phase="q"; G.rolled=isCamb(pos);
  renderSide();
  const z=$("#qzone");
  z.innerHTML=
    '<div class="qcard">'+
      '<span class="qcount">'+c.n+(G.rolled?' · case camembert 🧀':'')+'</span>'+
      '<span class="qcat" style="background:'+c.c+'">'+c.e+' '+c.n+'</span>'+
      '<h2 class="qtext">'+G.q.q+'</h2>'+
      '<div id="opts"></div>'+
      '<div class="fb" id="fb"></div>'+
      '<button class="next" id="next">Continuer →</button>'+
    '</div>';
  const o=$("#opts");
  G.q.o.forEach((t,k)=>{
    const b=document.createElement("button"); b.className="opt";
    b.innerHTML='<span class="k">'+"ABCD"[k]+'</span><span>'+t+'</span>';
    b.onclick=()=>answer(k); o.appendChild(b);
  });
  z.scrollIntoView({behavior:"smooth",block:"nearest"});
}
function answer(k){
  const p=G.players[G.turn], good=G.q.r, ci=G.ci;
  const opts=[...document.querySelectorAll(".opt")];
  opts.forEach((b,i)=>{b.disabled=true;if(i===good)b.classList.add("ok");if(i===k&&k!==good)b.classList.add("ko");});
  const fb=$("#fb"); let nextTurn=true, msg="";
  if(k===good){
    if(G.rolled && !p.parts.includes(ci)){
      p.parts.push(ci); msg="🧀 <b>Camembert gagné !</b> "; confetti(30);
      if(p.parts.length===6) return endGame(p);
    } else if(G.rolled){
      msg="✅ <b>Bonne réponse</b> — camembert déjà gagné. ";
    } else {
      msg="✅ <b>Bonne réponse !</b> Tu rejoues. "; nextTurn=false;
    }
    fb.className="fb good on"; fb.innerHTML=msg+(G.q.e||"");
  } else {
    fb.className="fb bad on";
    fb.innerHTML="❌ <b>Raté.</b> La bonne réponse : <b>"+G.q.o[good]+"</b>"+(G.q.e?" — "+G.q.e:"");
  }
  const nx=$("#next"); nx.style.display="block";
  nx.textContent = nextTurn ? "Joueur suivant →" : "Relancer le dé 🎲";
  nx.onclick=()=>{
    if(nextTurn) G.turn=(G.turn+1)%G.players.length;
    G.phase="roll"; $("#qzone").innerHTML="";
    draw(); renderSide();
  };
}
function endGame(p){
  show("v-win");
  $("#winbox").innerHTML='<div class="trophy">🏆</div><h2>'+p.name+' a les six camemberts !</h2>'+
    '<p>'+G.pak.nom+' · partie terminée en '+G.used.size+' questions.</p>'+
    '<button class="play" id="again" style="max-width:260px;margin:0 auto">Rejouer 🔁</button>';
  $("#again").onclick=()=>{show("v-setup");renderSetup();};
  confetti(130);
}
function confetti(n){
  const box=$("#conf"); box.innerHTML="";
  const cols=["#1E6FD9","#E8B31C","#A855F7","#22A06B","#F97316","#E8456B"];
  for(let i=0;i<n;i++){const c=document.createElement("i");c.className="cf";
    c.style.left=Math.random()*100+"vw";c.style.background=cols[Math.floor(Math.random()*cols.length)];
    c.style.animationDuration=(1.5+Math.random()*1.7)+"s";c.style.animationDelay=(Math.random()*0.5)+"s";
    box.appendChild(c);}
  setTimeout(()=>box.innerHTML="",4000);
}
renderSetup();
