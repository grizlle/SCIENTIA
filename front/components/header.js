import Link from "next/link";
import Image from "next/image";
import logo from '../public/logo.svg'
import styles from '../styles/Header.module.scss'

const Header = () => {
 return (
  <header className={styles.navbar}>
	  <Image src={logo} alt='logo'></Image>
	  <nav>
		  <Link href='/'>Домой</Link>
		  <Link href='/publications'>Публикации</Link>
		  <Link href='/authors'>Авторы</Link>
	  </nav>
  </header>
 );
};

export default Header;
