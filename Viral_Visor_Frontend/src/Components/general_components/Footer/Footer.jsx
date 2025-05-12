import "./Footer.css";
import logo from "../../../assets/General assets/logo.svg";

const Footer = () => {
  return (
    <div className="Footer">
      <div className="logo_title">
        <img src={logo} alt="" />
        <h1>Viral <span>Visor</span></h1>
      </div>

   
        <ul className="media_footer">
          <li>Viral Visor</li>
          <li>@ViralVisor</li>
        </ul>
        <ul className="Contact_footer">
          <li>+961 70777777</li>
          <li>Info@viralvisor.com</li>
        </ul>
   
    </div>
  );
};

export default Footer;
