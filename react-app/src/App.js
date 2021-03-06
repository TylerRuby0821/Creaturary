import React, { useEffect } from "react";
import { BrowserRouter, Route, Switch} from "react-router-dom";
import { useDispatch} from "react-redux";
import { authenticate } from "./store/session";
import {getCreatures} from './store/creature'
import {getTags} from './store/tag'
import {getImages} from './store/image'
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import LandingPage from './components/LandingPage/LandingPage'
import MainPage from './components/MainPage/MainPage'
import Creature from "./components/Creature/Creature";
import SearchLore from './components/Search/SearchLore'
import SearchAz from './components/Search/SearchAz'
import SearchCustom from './components/Search/SearchCustom'
import Search from './components/Search/Search'
import ProtectedRoute from './components/auth/ProtectedRoute'
import { getFavorites } from "./store/favorite";

function App() {
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(authenticate())
    dispatch(getFavorites())
  }, [dispatch]);

  useEffect(() => {
    dispatch(getCreatures())
    dispatch(getTags())
    dispatch(getImages())
  }, [dispatch])





  return (
    <BrowserRouter>
        <Switch>
          <Route path="/" exact={true}>
            <LandingPage />
          </Route>
          <Route path="/login" exact={true}>
            <LoginForm />
          </Route>
          <Route path="/sign-up" exact={true}>
            <SignUpForm />
          </Route>
          <ProtectedRoute path="/creatures" exact={true}>
            <MainPage />
          </ProtectedRoute>
          <ProtectedRoute path="/creatures/lore" exact={true}>
            <SearchLore />
          </ProtectedRoute>
          <ProtectedRoute path="/creatures/custom" exact={true}>
            <SearchCustom />
          </ProtectedRoute>
          <ProtectedRoute path="/creatures/a-z" exact={true}>
            <SearchAz />
          </ProtectedRoute>
          <ProtectedRoute path="/creatures/search" exact={true}>
            <Search />
          </ProtectedRoute>
          <ProtectedRoute path="/creatures/:creatureId" exact={true}>
            <Creature />
          </ProtectedRoute>
        </Switch>
    </BrowserRouter>
  );
}

export default App;
