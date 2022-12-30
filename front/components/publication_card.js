import styles from '../styles/PublicationCard.module.scss'
import Link from "next/link";
const PublicationCard = ({pub}) => {
 return (
  <div className={styles.publication_card}>
	  <div className={styles.title}><Link href={`/publications/${pub.id}`}>{pub.title}</Link></div>
	  {/*<div className={styles.title}>{pub.title}</div>*/}
	  <div className={styles.authors}>
		  {
			  pub.authors.map(author => {
				  return <Link key={author.id} href={`/authors/${author.id}`}>{author.fio}</Link>
			  })
		  }
	  </div>
	  <div className={styles.type}>{pub.cat}</div>
	  <div className={styles.year}>{pub.publication_year}</div>
  </div>
 );
};

export default PublicationCard;
