import React from 'react';
import { useSelector} from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import {useLocation} from 'react-router-dom'
import './Search.css'
// import {getCreatures} from '../../store/creature'
import Result from '../Result/Result'

const Search = () => {
  const query = useLocation()
  const test = query.search.slice(1)
  // const search = props.search
  // console.log('SEARCH', search)
  const allCreatures = useSelector(state => state.creature)
  // const dispatch = useDispatch();
  // const [creatures, setCreatures] = useState({})
  // console.log("Creatures = ", allCreatures)

  let creaturesArr = []
  for (const creat in allCreatures) {
    // console.log('CREAT', allCreatures[creat])
    // console.log('QUERY', query)
    // console.log('TEST', test)
    if (allCreatures[creat].name.toLowerCase().includes(test))
      creaturesArr.push(allCreatures[creat])
  }
  // console.log('ARRAY', creaturesArr)
  creaturesArr.sort((a, b) => {
    return a.name.localeCompare(b.name)  //Sort Function referenced from Stack Overflow
  })
  //https://stackoverflow.com/questions/8900732/sort-objects-in-an-array-alphabetically-on-one-property-of-the-array

  // useEffect(() => {
  //   setCreatures(dispatch(getCreatures()))
  // }, [dispatch])


  if(creaturesArr){
     creaturesArr.map(creature => {
      return (
        <Result key={creature.id} creature={creature}/>
      )

  })} else{
      return <div> No Creatures to display!</div>
  }




  return (
    <div>
      <Navigation />
      <div className='search__results'>
        {creaturesArr.length > 0 ?
          creaturesArr.map(creature => {
            return (
              <Result key={creature.id} creature={creature}/>
            )

        })
          : <div className='null__result'>No Creature under that name.. yet!</div>
        }

      </div>
  </div>
  )
}

export default Search
