import React from "react"

function Message({query, response}) {
  return(
  <div>
    <p className="query">{query}</p>
    <p className="response">{response}</p>
  </div>
  )

}

export default Message