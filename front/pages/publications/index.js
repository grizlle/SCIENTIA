import PublicationCard from "../../components/publication_card";

const Publications = ({publications}) => {
 return (
  <div>
    <h1>Публикации</h1>
      {publications.map(pub => {
         return <PublicationCard key={pub.id} pub={pub}/>
        })
      }

  </div>
 );
};

export default Publications;
export async function getServerSideProps() {
    const resp = await fetch('http://127.0.0.1:8000/api/v1/publications/');
    const data = await resp.json();

    return {
        props: {
            publications: data
        }
    }
}
