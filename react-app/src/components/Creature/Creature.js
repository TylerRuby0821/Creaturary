import React, {useEffect, useState} from 'react';
import { Redirect, NavLink, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import './Creature.css'
import Navigation from '../Naviagtion/Navigation';
import { getCreature } from '../../store/creature';


const Creature = () => {

  const allCreatures = useSelector(state => state.creature)
  // console.log('ALL CREATURES',allCreatures)
  const { creatureId } = useParams();
  // console.log(allCreatures[0].name)
  let creature = {};
  for (const creat in allCreatures) {
    // console.log("CREAT", allCreatures[creat].id)
    if (allCreatures[creat].id === parseInt(creatureId)){
      creature = {...allCreatures[creat]}

   }
  }

  // console.log(creature)
  // console.log(creature)
  // const dispatch = useDispatch()
  // allCreatures.forEach(creat => {
  //   if (creature.id === creatureId){
  //      creature = creat
  //   }
  // });
  // const creatures = useSelector(state => state.creature)
  // console.log("CREATURES", creatures)
  // useEffect(() => {
  //   (async () => {
  //       const creat = await dispatch(getCreature(creatureId))
  //       setcurrCreature(creat)
  //   })()

  // }, [creatureId, dispatch])

  return (
    <div>
      <Navigation />
      {/* Thumbnail */}
      <div className='main__body--creature'>
        <span className='creature__name'>{creature.name}</span>
        <span className='creature__tag'>{creature.tag_id}</span>
        <div className='creature__decription'>{creature.description}</div>
      </div>
    </div>
    )
}

export default Creature;
