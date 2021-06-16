import React, { useState} from 'react';
import './Pagination.css'

const Pagination = ({data, Result, title, pageLimit, creatures}) => {
  const [currentPage, setCurrentPage] = useState(1)
  const [pages] = useState(Math.round(data.length / creatures))
  pageLimit = pages
  const nextPage = () => {
    setCurrentPage((page) => page + 1)
  }

  const prevPage = () => {
    setCurrentPage((page) => page - 1)
  }

  // const jumpPage = () => {
  //   const jumpPage = ((event) => console.log(event))

  //   setCurrentPage(jumpPage)
  // }

  const getResults = () => {
    const startInd = currentPage * creatures - creatures
    const endInd  = startInd + creatures
    return data.slice(startInd, endInd)
  }

  // const pageNumbers = () => {
  //   let start = Math.floor((currentPage - 1) / pageLimit) * pageLimit
  //   return new Array(pageLimit).fill().map((_, idx) => Number(start + idx + 1))
  // }

  return (
    <>
      <h1 className='pagination__title'>{title}</h1>
      <div>
        {getResults().map((d, idx) =>(
          <Result key={idx} data={d} />
        ))}
      </div>
      <div>
        {/* Previous Button */}
          <button
          onClick = {prevPage}
          className={`prev ${currentPage === 1 ?  'disabled' : ''}`}
          >
            Previous
          </button>

          {/* {pageNumbers().map((item, index) => (
            <button
            key={index}
            onClick={jumpPage}
            className={`pageNumbers ${currentPage === item ? 'active' : null}`}
            >
              {item}
            </button>
          ))} */}
          <button
          onClick = {nextPage}
          className={`next ${currentPage === pages ?  'disabled' : ''}`}
          >
            Next
          </button>
      </div>
    </>
  )

}

export default Pagination
