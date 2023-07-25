<template>
   <div class="card-container">
        <div class="card">
            <div class="card-title">Sau reservoir</div>
            <img src="../assets/sau.jpg" alt="Image 1">
        </div>
        <div class="card">
            <div class="card-title">Llosa del cavall</div>
            <img src="../assets/llosa-del-cavall.jpg" alt="Image 2">
        </div>
        <div class="card">
            <div class="card-title">Sant Ponç</div>
            <img src="../assets/sant-ponç.jpg" alt="Image 3">
        </div>
        <div class="card">
            <div class="card-title">Foix</div>
            <img src="../assets/foix.jpg" alt="Image 4">
        </div>
    </div>
</template>

<style scoped>

.card-container {
    align-items: center;
    justify-content: center;
    width: 1600px;
    display: grid;
    margin: 20px auto 0 auto;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    grid-gap: 100px;
    padding: 0;
}

@media (max-width: 800px) {
    .card-container {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    }
}

@media (max-width: 500px) {
    .card-container {
        grid-template-columns: repeat(1, 1fr);
    }
}

.card {
    width: 350px;
    border-radius: 5px;
    margin: 30px;
    background-color: white;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 2px;
}

.card-title {
    font-weight: bold;
    text-align: center;
    padding: 8px;
    background-color: #ffffff;
    border-radius: 5px 5px 0 0;
}

.card img {
    width: 100%;
    height: 230px;
    object-fit: cover; 
    display: block;
    border-radius: 5px;
}

ul {
    display: flex;
    float: none;
    clear: both;
    overflow: hidden;
    margin: auto;
    justify-content: center;
    margin: 60px auto 20px auto;
}

@media screen and (max-width: 480px) {
    .card {
        width: 100%;
        height: auto;
        padding: 0;
    }
}

article {
    background-color: #fff;
    padding: 10px;
    border: 0px solid #ccc;
    border-radius: 5px;
    font-size: 18px;
    text-align: start;
    color: black;
}

.tooltip-data {
   margin-bottom: 15px;
}

.disclaimer {
   font-size: 12px;
   color: #00000077;
   margin: 100px 0 0 0;
   text-align: start;
   margin-top: -8px;
}
</style>