import React from 'react';
import useSWR from "swr";
import {fetchPublications} from "@/api/publications";
import {Publication} from "@/components/shared/interfaces";
import PublicationCard from "@/components/Publications/PublicationCard";

const PublicationsList = () => {

    const {data, isLoading, error} = useSWR<Publication[]>(['api/publications/'],
        ([url]: [string]) => fetchPublications(url), {revalidateIfStale: false});

    if(isLoading) return null
    if(error) return null
    return (
        <div className="publication__list">
            {data?.map((item) => <PublicationCard key={item.id} publication={item}/>)
            }
        </div>
    );
};

export default PublicationsList;
