(function(){
var C=window.CB_HELP||{},T=C.t||{},pf=null;
function load(){if(!pf){pf=import(C.base+'pagefind/pagefind.js').then(function(p){p.options({excerptLength:22});p.init();return p})}return pf}
document.querySelectorAll('.hs').forEach(function(f){
var inp=f.querySelector('.hs-i'),ul=f.querySelector('.hs-r'),act=-1,res=[],seq=0,tm,ga;
function msg(t){ul.textContent='';var li=document.createElement('li');li.className='none';li.textContent=t;ul.appendChild(li);ul.classList.add('on')}
function hl(){ul.querySelectorAll('a').forEach(function(a,i){a.classList.toggle('act',i===act)})}
function run(){var q=inp.value.trim(),my=++seq;if(!q){ul.classList.remove('on');res=[];return}
load().then(function(p){return p.debouncedSearch(q,{},120)}).then(function(r){if(!r||my!==seq)return null;return Promise.all(r.results.slice(0,12).map(function(x){return x.data()}))}).then(function(d){
if(!d||my!==seq)return;
d.sort(function(a,b){return (a.meta.legacy?1:0)-(b.meta.legacy?1:0)});res=d.slice(0,8);act=res.length?0:-1;
clearTimeout(ga);ga=setTimeout(function(){if(window.gtag)gtag('event','search',{search_term:q,results:res.length})},1500);
if(!res.length){msg(T.noresult);return}
ul.textContent='';res.forEach(function(r){var li=document.createElement('li'),a=document.createElement('a'),t=document.createElement('span'),b=document.createElement('b'),c=document.createElement('span'),x=document.createElement('span');
a.href=r.url;if(r.meta.legacy)a.className='old';t.className='hs-t';b.textContent=r.meta.title;c.textContent=r.meta.cat||'';t.appendChild(b);t.appendChild(c);x.className='hs-x';x.innerHTML=r.excerpt;a.appendChild(t);a.appendChild(x);li.appendChild(a);ul.appendChild(li)});
hl();ul.classList.add('on')}).catch(function(){msg(T.noresult)})}
inp.addEventListener('focus',function(){load();if(inp.value.trim())run()});
inp.addEventListener('input',run);
inp.addEventListener('keydown',function(e){
if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();if(res.length){act=(act+(e.key==='ArrowDown'?1:res.length-1))%res.length;hl();var a=ul.querySelectorAll('a')[act];a&&a.scrollIntoView({block:'nearest'})}}
else if(e.key==='Enter'){e.preventDefault();if(act>=0&&res[act])location.href=res[act].url}
else if(e.key==='Escape'){ul.classList.remove('on');inp.blur()}});
document.addEventListener('click',function(e){if(!f.contains(e.target))ul.classList.remove('on')})});
document.addEventListener('keydown',function(e){var i=document.querySelector('.hs-i');if(!i)return;
if((e.key==='k'&&(e.ctrlKey||e.metaKey))||(e.key==='/'&&!/input|textarea/i.test(document.activeElement.tagName))){e.preventDefault();i.focus();i.select()}});
if(/Mac|iPhone|iPad/.test(navigator.platform))document.querySelectorAll('.hs-k').forEach(function(k){k.textContent='⌘K'});
var fb=document.querySelector('.fb');if(fb)fb.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
if(window.gtag)gtag('event','help_feedback',{useful:b.dataset.v,page:location.pathname});
fb.querySelectorAll('button').forEach(function(x){x.hidden=true});fb.querySelector('em').hidden=false});
})();
