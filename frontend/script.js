const searchBtn=document.getElementById("searchBtn");
const searchName=document.getElementById("searchName");
const priceLow=document.getElementById("priceRangeLow");
const priceHigh=document.getElementById("priceRangeHigh");
const results=document.getElementById("results");

searchBtn.addEventListener("click",async()=>{
    const name=searchName.value;
    const min_price=priceLow.value*100 || 0;
    const max_price=priceHigh.value*100 || 999999;
    if(!name){
        results.innerHTML=`<p>Enter a name to search.</p>'`;
        return;
    }
    results.innerHTML=`<p>Searching...</p>`;
    try{
        const res=await fetch(`http://127.0.0.1:8000/get/games?q=${encodeURIComponent(name)}&min_price=${min_price}&max_price=${max_price}&limit=10`);
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
            <h3>${g.name}</h3>
            <h3>${g.developer}</h3>
            <h3>$${g.initialprice*0.01}</h3>
            <h3>$${g.price*0.01}</h3>
        </div>
    `).join('');
}