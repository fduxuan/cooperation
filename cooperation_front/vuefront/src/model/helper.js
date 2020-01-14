import axios from "axios"




//let baseURL = "http://localhost:8000"
let baseURL = "http://116.62.46.96:3000"
export async function Get(url) {
    let res = await axios.get(baseURL+url)
    return res.data
}


export async function Post(url, data=undefined) {
    let res = await axios.post(baseURL+url,JSON.stringify(data))
    return res.data
}
