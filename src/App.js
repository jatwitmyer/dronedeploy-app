import React, { useEffect, useState } from "react";
import Card from "./Card";
import Message from "./Message"

function App() {
  //storage for fetched data
  const [data, setData] = useState([])
  const [messages, setMessages] = useState([])
  //chatbot text visibility
  const [chatIsVisible, setChatIsVisible] = useState(true)
  function showChat() {
    setChatIsVisible(true)
  }
  //featured image overlay
  const [featuredImage, setFeaturedImage] = useState({'src':'', 'alt':''})
  const [featuredImageIsVisible, setFeaturedImageIsVisible] = useState(false)

  //preload images separately from data fetch for UI responsiveness for slow connections
  const galleryImages = ["YNP_001.jpg", "YNP_002.jpg", "YNP_003.jpg", "YNP_004.jpg", "YNP_005.jpg"];
  let gallery = galleryImages.map((image_name, index) => <Card key={index} image_name={image_name}/>);
  
  // fetch data for displayed images
  useEffect(() => {
    fetch('http://127.0.0.1:5000/data')
      .then(response => response.json())
      .then(data => {
        setData(data)
      })
      .catch(error => {
        console.error('Error fetching data:', error)
      })
  }, [])
  // console.log(data)
  
  // render data
  if (data.length > 0) {
    gallery = data.map((image_data, index) => <Card key={index} image_name={image_data.file_name} image_data={image_data} setFeaturedImageIsVisible={setFeaturedImageIsVisible} setFeaturedImage={setFeaturedImage}/>)
  }

  function handleSubmit(e) {
    e.preventDefault()
    const query = document.getElementById("search").value
    fetch('http://127.0.0.1:5000/query', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({user_query: query})
    })
    .then(r => r.json())
    .then(response => {
      console.log(response)
      setMessages([...messages, {"query": query, "response": response.message}])
    })
  }

  let displayMessages = <></>
  if (messages.length > 0) {
    displayMessages = messages.map((pair) => <Message query={pair.query} response={pair.response}/> )
  }

  function handleClickAway(e) {
    if (e.target.tagName === 'DIV') {
      setFeaturedImageIsVisible(false)
    }
  }

  return (
    <div id="App">
      <header>
        <img onClick={(e) => showChat()} id="chatbot" src={process.env.PUBLIC_URL + "Chatbot Chat Message.jpg"} alt="chatbot"></img>
        <h1>DroneDeploy Gallery</h1>
      </header>
      <div id="chatbot-overlay" style={{visibility: chatIsVisible ? 'visible' : 'hidden' }}>
        <button className="hide-overlay" onClick={(e) => setChatIsVisible(false)}>X</button>
        <p id="prompt">Have a question about an image? Ask our chatbot: </p>
        <form id="searchbar" onSubmit={e => handleSubmit(e)}>
          <input type="text" id="search" placeholder="What is the altitude of the second image?" />
          <button id="search-button">Search</button>
        </form>
        <div id="message-history">
          {displayMessages}
        </div>
      </div>
      <div onClick={(e) => handleClickAway(e)} id="image-overlay"  style={{visibility: featuredImageIsVisible ? 'visible' : 'hidden' }}>
        <button className="hide-overlay" id="hide-featured-image" onClick={(e) => setFeaturedImageIsVisible(false)}>X</button>
        <img src={featuredImage.src} alt={featuredImage.name}></img>
      </div>
      <main>
        <div id="Gallery">
          {gallery}
        </div>
      </main>
      <footer><div><p>Displaying 5 of 5 images</p></div></footer>
    </div>
  );
}

export default App;
