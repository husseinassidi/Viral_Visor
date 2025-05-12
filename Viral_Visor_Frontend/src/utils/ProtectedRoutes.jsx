import { Outlet,Navigate } from "react-router-dom";


const ProtectedRoutes = ()=>{

    const user =sessionStorage.getItem("user_id");
    return(
        user!= null? <Outlet/>:<Navigate to="/"/>
    )


}


export default ProtectedRoutes;