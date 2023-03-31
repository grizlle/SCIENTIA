import Link from "next/link";
import {Publication} from "@/components/shared/interfaces";
import styles from './PublicationCard.module.scss'
import router from "next/router";

interface PublicationCardProps {
    publication: Publication
}
const PublicationCard = ({publication}: PublicationCardProps) => {
    return (
        <div className={styles.publication_card} onClick={() => {router.push(`/publications/${publication.id}`)}}>
            <div className={styles.topContent}>
                <div className={styles.title}>{publication.title}</div>
                <div className={styles.download}>
                    <img src="/download.svg" />
                </div>
            </div>
            <div className={styles.bottomContent}>
                <div className={styles.authors}>
                    {
                        publication.authors.map(author => {
                            return <Link key={author.id} href={`/authors/${author.id}`}>{author.fio}</Link>
                        })
                    }
                </div>
                <div className={styles.otherInfo}>
                    <div className={styles.type}>{publication.cat}</div>
                    <div className={styles.year}>{publication.publication_year}</div>
                </div>
            </div>
        </div>
    );
};

export default PublicationCard;

