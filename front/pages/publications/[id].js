import styles from '../../styles/PublicationPage.module.scss'
import Image from "next/image";
import default_avatar from "../../public/default_avatar.png"
import logo from "../../public/logo.svg";

const Publication = ({publication}) => {
	return (
	  <div className={styles.publication}>

		  <div className={styles.publication__title__wrapper}>
			  <div className={styles.publication__title}>{publication.title}</div>
			  <div className={styles.publication__cat}>{publication.cat}</div>
		  </div>


		  <div className={styles.publication__authors}>
			  <div className={styles.publication__authors__title}>Авторы</div>
			  {	publication.authors.map(author => {
				  return (<div key={author.id} className={styles.publication__authors__author}>
					  {author.avatar_url ? <Image></Image> : <Image src={default_avatar} alt='avatar'></Image>}

					  <div className={styles.publication__authors__author__name}>{author.fio}</div>
				  </div>)
			  })
			  }
		  </div>
	  </div>
 	);
};

export default Publication;

export async function getServerSideProps(router) {
	const resp = await fetch('http://127.0.0.1:8000/api/v1/publications/' + router.query.id);
	const data = await resp.json();

	return {
		props: {
			publication: data
		}
	}
}
