import React from 'react';
import PublicationsList from "@/components/Publications/PublicationsList";
import Filters from "@/components/Publications/Filters";
import styles from "./PublicationsPage.module.scss"

const PublicationsPage = () => {

    return (
        <div className={styles.publicationPage}>
            <div className="container">
                <div className={styles.content}>
                    <Filters/>
                    <PublicationsList/>
                </div>
            </div>
        </div>
    );
};

export default PublicationsPage;
