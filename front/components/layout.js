import Header from "./header";
import Footer from "./footer";

const Layout = ({children}) => {
 return (
  <div className='content'>
	  <Header></Header>
	  	{children}
	  <Footer></Footer>
  </div>
 );
};

export default Layout;
