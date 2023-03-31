import {Publication, PublicationDetail} from "@/components/shared/interfaces";
import {api} from "@/api/config";

export async function fetchPublications(url: string): Promise<Publication[]> {
    const response = await api.get(url);
    return response.json();
}

export async function fetchPublicationDetail(url: string): Promise<PublicationDetail> {
    const response = await api.get(url);
    return response.json();
}
