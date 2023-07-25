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
    width: 1080px;
    display: grid;
    margin: 60px auto 20px auto;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    grid-gap: 200px;
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
    transition: transform 0.3s ease;
}

.card:hover {
    transform: scale(1.01); /* Increase the scale on hover to create the pop-up effect */
}

.card-title {
    font-weight: bold;
    text-align: center;
    padding: 10px;
    background-color: #fff;
    border-radius: 5px 5px 0 0;
}

.card img {
    width: 100%;
    height: 230px;
    object-fit: cover; 
    display: block;
    border-radius: 0 0 5px 5px;
}

.card-inner:hover {
    box-shadow: 0px 0px 15px 2px rgba(0, 0, 0, 0.5);
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
.card {
    height: fit-content;
    margin: 0 0 10px 0;
    padding: 0 20px 20px 20px;
    list-style: none;
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