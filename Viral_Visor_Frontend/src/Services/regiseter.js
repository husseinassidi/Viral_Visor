import axios from 'axios'



    const register_service  = async (data) => {

        const config = {
            headers: {
                'Content-Type': 'application/json',
                'User-Agent': 'PostmanRuntime/7.42.0',
                'Accept': '*/*',
            }
        };
        
        axios.post('http://127.0.0.1:8080/register/', data, config)
            .then(response => {
                console.log('Response:', response.data);
            })
            .catch(error => {
            if (error.response && error.response.data) {
                setResponseMessage("Error: " + error.response.data.detail);
            } else {
                setResponseMessage("Error submitting form.");
            }
            });
        

    }

    
        // try {
        //     const response = await axios.post('http://127.0.0.1:8080/register/', formData, {
        //         headers: {
        //             'Content-Type': 'application/json',
        //             'Accept-Encoding': 'gzip, deflate, br',
        //             'Connection': 'keep-alive'
        //         }
        //     });
        //     setResponseMessage("Registration Successful: " + JSON.stringify(response.data));
        // } catch (error) {
        //     if (error.response && error.response.data) {
        //         setResponseMessage("Error: " + error.response.data.detail);
        //     } else {
        //         setResponseMessage("Error submitting form.");
        //     }
        // }

    export default register_service;