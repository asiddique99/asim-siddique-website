(function(){
  function el(tag, cls, text){var e=document.createElement(tag); if(cls) e.className=cls; if(text!=null) e.textContent=text; return e;}
  function fmt(d){var p=String(d).split('-'); var dt=new Date(Date.UTC(+p[0],(+p[1]||1)-1,+p[2]||1)); return dt.toLocaleDateString('en-US',{year:'numeric',month:'long',day:'numeric',timeZone:'UTC'});}
  function safeUrl(u){try{var x=new URL(u); return (x.protocol==='https:'||x.protocol==='http:')?x.href:null;}catch(e){return null;}}
  function getJSON(u){return fetch(u,{cache:'no-store'}).then(function(r){if(!r.ok) throw new Error(r.status); return r.json();});}
  function load(limit){
    return getJSON('/posts/index.json').then(function(d){
      var ids=((d&&d.posts)||[]).filter(function(x){return /^\d{4}-\d{2}-\d{2}$/.test(x);}).sort().reverse();
      if(limit) ids=ids.slice(0,limit);
      return Promise.all(ids.map(function(id){return getJSON('/posts/'+id+'.json').catch(function(){return null;});}));
    }).then(function(ps){return ps.filter(function(p){return p&&p.title;});});
  }
  window.__blog={el:el,fmt:fmt,safeUrl:safeUrl,load:load};
})();
