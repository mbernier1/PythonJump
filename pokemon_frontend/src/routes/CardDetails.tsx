import React from 'react'
import { Form } from "react-router-dom"

const CardDetails = () => {
    const contact = {
        first: "Your",
        last: "Name",
        avatar: "https://placekitten.com/g/200/200",
        twitter: "your_handle",
        notes: "Some notes",
        favorite: true,
      };
    
      return (
        <div className='card-details-main bg-white w-full max-w-screen-md'>
          <div>
            <img
              key={contact.avatar}
              src={contact.avatar}
            />
          </div>
    
          <div className=''>
            <h1>
              {contact.first || contact.last ? (
                <>
                  {contact.first} {contact.last}
                </>
              ) : (
                <i>No Name</i>
              )}{" "}
              <Favorite contact={contact} />
            </h1>
    
            {contact.twitter && (
              <p>
                <a
                  target="_blank"
                  href={`https://twitter.com/${contact.twitter}`}
                >
                  {contact.twitter}
                </a>
              </p>
            )}
    
            {contact.notes && <p>{contact.notes}</p>}
    
            <div>
              <Form action="edit">
                <button type="submit">Edit</button>
              </Form>
              <Form
                method="post"
                action="destroy"
                onSubmit={(event) => {
                  if (
                    !confirm(
                      "Please confirm you want to delete this record."
                    )
                  ) {
                    event.preventDefault();
                  }
                }}
              >
                <button type="submit">Delete</button>
              </Form>
            </div>
          </div>
        </div>
      );
    }
    
    function Favorite({ contact }: any) {
      // yes, this is a `let` for later
      let favorite = contact.favorite;
      return (
        <Form method="post">
          <button
            name="favorite"
            value={favorite ? "false" : "true"}
            aria-label={
              favorite
                ? "Remove from favorites"
                : "Add to favorites"
            }
          >
            {favorite ? "★" : "☆"}
          </button>
        </Form>
      );
}

export default CardDetails