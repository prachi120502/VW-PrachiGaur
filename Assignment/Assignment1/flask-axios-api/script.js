async function runApp(){

    // Add product
    const create = await axios.post(
        "http://localhost:5000/api/products",
        {
            name:"Smart Watch",
            price:4500
        }
    )

    console.log("Product Created:", create.data)


    // Fetch products AFTER adding
    const products = await axios.get(
        "http://localhost:5000/api/products"
    )

    console.log("All Products:", products.data)


    // Fetch external API
    const external = await axios.get(
        "https://api.sampleapis.com/futurama/info"
    )

    console.log("External API Data:", external.data)


    // Send external API data to Flask
    await axios.post(
        "http://localhost:5000/api/products",
        external.data
    )

    console.log("External API data pushed to Flask API")

}

runApp()