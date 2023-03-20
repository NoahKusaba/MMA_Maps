const express = require("express")
const app = express()
const port = 3001
const database_data = require("./get_db")

app.use(express.json())
app.use(function (req, res, next){
    res.setHeader("Access-Control-Allow-Origin", "http://localhost:3000");
    res.setHeader("Access-Control-Allow-Methods", "GET");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers");
    next();
})

app.get("/", (req,res) => {
    database_data.get_db()
    .then(response => {
        res.status(200).send(response);
    })
    .catch(error =>{
        res.status(500).send(error);
    })
})

app.get("/TestData", (req,res) =>{
    res.status(200).send();

})

app.listen(port, () => {
    console.log("App running on port $ {port} .")
})