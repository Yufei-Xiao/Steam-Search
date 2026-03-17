const searchNameBtn=document.getElementById("searchNameBtn");
const searchName=document.getElementById("searchName");
const results=document.getElementById("results");
searchNameBtn.addEventListener("click",async()=>{
    const name=searchName.value;
    if(!name){
        results.innerHTML=`<p>Enter a name to search.</p>'`;
        return;
    }
    results.innerHTML=`<p>Searching...</p>`;
    try{
        const res=await fetch(`http://127.0.0.1:8000/api/games?q=${encodeURIComponent(name)}&limit=10`);
        if(!res.ok) throw new Error(res.statusText);
        const data=await res.json();
        renderResults(data);
    }catch(error){
        results.innerHTML=`<p>Error: ${error.message}</p>`;
    }
})

function renderResults(data){
    if (!data || !data.results || data.total===0){
        results.innerHTML=`<p>No results</p>`;
        return;
    }
    results.innerHTML=data.results.map(g=>`
        <div class="game">
            <h1>${g.appid}
            <h1>${g.name}</h1>
            <h1>${g.developer}</h1>
        </div>
    `).join('');
}