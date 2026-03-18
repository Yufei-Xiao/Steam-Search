const searchBtn=document.getElementById("searchBtn");
const searchName=document.getElementById("searchName");
const developer=document.getElementById("developer");
const publisher=document.getElementById("publisher");
const playtimeLow=document.getElementById("playtimeLow");
const playtimeHigh=document.getElementById("playtimeHigh");
const priceLow=document.getElementById("priceRangeLow");
const priceHigh=document.getElementById("priceRangeHigh");
const results=document.getElementById("results");

searchBtn.addEventListener("click",async()=>{
    const name=searchName.value;
    const dev=developer.value;
    const pub=publisher.value;
    const playtime_min=playtimeLow.value || "";
    const playtime_max=playtimeHigh.value || "";
    const min_price=priceLow.value*100 || 0;
    const max_price=priceHigh.value*100 || 999999;
    
    results.innerHTML=`<p>Searching...</p>`;
    // Build query string
    let url = `http://127.0.0.1:8000/get/games?q=${encodeURIComponent(name)}&min_price=${min_price}&max_price=${max_price}&limit=20`;
    if(dev) url += `&developer=${encodeURIComponent(dev)}`;
    if(pub) url += `&publisher=${encodeURIComponent(pub)}`;
    if(playtime_min) url += `&playtime_min=${encodeURIComponent(playtime_min)}`;
    if(playtime_max) url += `&playtime_max=${encodeURIComponent(playtime_max)}`;
    try{
        const res=await fetch(url);
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
            <h3>Name: ${g.name}</h3>
            <h3>Developer: ${g.developer}</h3>
            <h3>Publisher: ${g.publisher}</h3>
            <h3>Initial Price: $${g.initialprice*0.01}</h3>
            <h3>Current Price: $${g.price*0.01}</h3>
            <h3>Owners: ${g.owners}</h3>
            <h3>Average Playtime: ${(parseInt(g.average_forever)/60).toFixed(1)}</h3>
        </div>
    `).join('');
}