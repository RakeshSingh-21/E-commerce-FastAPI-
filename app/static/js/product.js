function parseJwt(token) {
    const base64Url = token.split('.')[1]
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
    }).join(''))

    return JSON.parse(jsonPayload)
}

const token = localStorage.getItem("token")

if(token){
    const user = parseJwt(token)

    if(user.role === "admin"){
        document.getElementById("addProductBtn").style.display="inline-block"
    }else{
        document.getElementById("addProductBtn").style.display="none"
    }
}


async function loadProducts(){

const res = await fetch("/products")

const data = await res.json()

let rows=""

data.forEach(p => {

rows+=`

<tr>

<td>${p.id}</td>
<td>${p.name}</td>
<td>${p.price}</td>
<td>${p.description}</td>

<td>

<button onclick="orderProduct(${p.id})">Order</button>

</td>

</tr>

`

})

document.getElementById("productTable").innerHTML=rows

}


async function orderProduct(product_id){

await fetch("/orders",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

user_id:1,
product_id:product_id

})

})

alert("Order placed!")

}

loadProducts()