export class dataControl { 

    constructor (container) {
        this.container = container
        console.log('Constructing')
        this.data = {}
        this.getData('/api')
      }

    async getData(api) {
        try {
            // get from API
            const feched = await fetch(api)
            // check for valid response
            const response = await status(feched)
            // get the json from the response
            const data = await response.json()

            this.data = data
            console.log(data)
            
        } catch (error) {
            // handle error
            console.log('error')
            console.log(error)
            }
    }
}

// promise helper function to determine if a http status represents a valid responce
function status (response) {
    if (response.status >= 200 && response.status < 300) {
      return Promise.resolve(response)
    } else {
      return Promise.reject(new Error(response.statusText))
    }
  }