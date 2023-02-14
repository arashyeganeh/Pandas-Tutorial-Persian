const dataset = [
    {
        Name: "Arash",
        Physic: 15,
        Chemistry: 16,
        Mathematic: 14
    },
    {
        Name: "Shahram",
        Physic: 15.25,
        Chemistry: 16,
        Mathematic: 10
    },
    {
        Name: "Omid",
        Physic: 18,
        Chemistry: 10,
        Mathematic: 15
    },
    {
        Name: "Morteza",
        Physic: 17,
        Chemistry: 9,
        Mathematic: 12
    },
    {
        Name: "Najme",
        Physic: 8,
        Chemistry: 15,
        Mathematic: 13
    },
    {
        Name: "Mahsa",
        Physic: 14,
        Chemistry: 19,
        Mathematic: 15.75
    },
    {
        Name: "Elham",
        Physic: 18,
        Chemistry: 16.25,
        Mathematic: 16
    },
    {
        Name: "Maryam",
        Physic: 17,
        Chemistry: 12.5,
        Mathematic: 19
    },
    {
        Name: "Sanam",
        Physic: 13,
        Chemistry: 19,
        Mathematic: 14
    }
]

const http = require("http")
const PORT = process.env.PORT || 3000;
const server = http.createServer(async (req, res) => {
    if (req.method !== "GET") {
        res.writeHead(404, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ message: "Not found :(" }));
        return;
    }
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(dataset));
});

server.listen(PORT, () => {
    console.log(`Server started on port: ${PORT} \n:)`)
    console.log(`Tip: "http" => default port is 80`)
    console.log(`Tip: "https" => default port is 443`)
})