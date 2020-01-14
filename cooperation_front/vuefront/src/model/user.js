import {Post, Get} from "./helper"

export async function getUserInfo() {
  let res = await Get('/api/user/info')
  console.log(res)
  return res

}
