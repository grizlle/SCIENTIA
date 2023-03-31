export type PublicationsList = Publication[]

export interface Publication {
    id: number
    authors: Author[]
    title: string
    publication_year: string
    cat: string
}

export interface Author {
    id: number
    fio: string
    avatar_url: any
}

export interface PublicationDetail {
    id: number
    authors: Author[]
    cat: string
    title: string
    sources: string
    abstract: string
    publication_year: string
    keywords: string
    output_data: string
    number: string
    tome: string
    issue_number: string
    pages: string
    details_of_documents: string
    udk: string
    publication_date: any
    description: string
    time_create: string
    time_update: string
    file_url: any
}
