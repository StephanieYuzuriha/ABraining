import config from "@/config.js";

function getUserId() {
  const userJson = localStorage.getItem("auth");
  const user = JSON.parse(userJson);
  console.log(user)
  return user.id;
}

// function getAccessToken() {
//   const jwtJson = localStorage.getItem("auth");
//   const jwt = JSON.parse(jwtJson);
//   return jwt.access_token;
// }


export async function addResults(results) {
  console.log("***ADD" + getUserId())
  const settings = {
      method: "POST",
      headers: { "Content-Type": "application/json",
                  Authorization: getUserId()  },
      body: JSON.stringify(results),
    };

    fetch(`${config.API_PATH}/results`, settings);
}

export async function getResults(){
   const settings = {
        method: "GET",
        headers: {
          Authorization: getUserId()  
        },
      };
      
      const response = await fetch(`${config.API_PATH}/results`, settings);
      if (response.status !== 401) {
        const results = await response.json()
        return results
      }
      else{
        return false
      }
      

}