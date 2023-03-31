import React from 'react';
import useSWR from "swr";
import Image from "next/image";
import styles from './PublicationDetailPage.module.scss';
import {Author, PublicationDetail} from "@/components/shared/interfaces";
import {fetchPublicationDetail} from "@/api/publications";

function PublicationDetailPage({query}: any) {
    const {data, isLoading, error} = useSWR<PublicationDetail>([`api/publications/${query.id.id}/`],
        ([url]: [string]) => fetchPublicationDetail(url), {revalidateIfStale: false});

    if (isLoading) return null
    if (error) return null
    if (data) return (
        <div className={styles.publicationPage}>
            <div className="container">
                <div className={`card ${styles.header}`}>
                    <div className={styles.title}>{data.title}</div>
                    <div className={styles.category}>{data.cat}</div>
                </div>
                <div className={styles.splitter}>
                    <div className={`${styles.mainInfo} card`}>
                        <div className={styles.infoItem}><span>Анотация: </span> {data.abstract}</div>
                        <div className={styles.infoItem}><span>Ключевые слова: </span> {data.keywords}</div>
                        <div className={styles.infoItem}><span>Источники: </span> {data.sources}</div>
                    </div>
                    <div className={styles.otherInfo}>
                        <div className={`${styles.authors} card`}>
                            <p>Авторы</p>
                            {data.authors.map((author: Author) => <div className={styles.authorItem}>
                                {author.avatar_url ?
                                    <div className={styles.authorAvatar}>
                                        <Image src={author.avatar_url} alt="avatar" fill/>
                                    </div>
                                    : <div className={styles.authorAvatar}>
                                        {author.fio[0]}
                                    </div>
                                }
                                <div>{author.fio}</div>
                            </div>)
                            }
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default PublicationDetailPage;

export async function getServerSideProps({query}: any) {
    return {props: {query: {id: query}}};
}
