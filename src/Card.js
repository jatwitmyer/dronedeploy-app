import React from 'react';

function Card({image_name, image_data, setFeaturedImageIsVisible, setFeaturedImage}) {
  let dataDisplay = <></> //placeholder while loading data

  if (image_data) {
    const dataPoints = Object.keys(image_data) //array of data keys
    dataDisplay = dataPoints.map(key => {
      let value = image_data[key]
      if (typeof value == 'object') {
        value = value.join(", ")
      }
      return <li className={key}> {key}: {value} </li>
    })
  }

  function handleClick(e) {
    console.log(e.target.src)
    console.log(e.target.alt)
    // setFeaturedImage(e.target)
    setFeaturedImageIsVisible(true)
    setFeaturedImage({'src':`${e.target.src}`, 'alt':`${e.target.alt}`})
  }

  return (
    <div className={image_name}>
      <img onClick={(e) => {handleClick(e)}} src={process.env.PUBLIC_URL + "/gallery_images/" + image_name} alt={image_name} />
      <div>
        <h4>Image Details</h4>
        <ul>
          {dataDisplay}
        </ul>
      </div>
    </div>
  );
}

export default Card;