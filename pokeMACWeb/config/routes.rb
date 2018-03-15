Rails.application.routes.draw do
  get 'welcome/index', to: "welcome#index", as: :welcome
  get "welcome/positions", to: "welcome#positions", as: :positions  
  get "pokedex/quest", to: "pokedex#quest", as: :quest
  get "questions/:id", to: "questions#show", as: :preg
  get "pokedex/pokelist", to: "pokedex#pokelist", as: :pokelist
  get "pokedex/pokemons", to: "pokedex#show", as: :pokemons
  get "pokedex/view_pokemon", to: "pokedex#view_pokemon", as: :view_pokemon
  get "pokedex/view_pokemon/:id", to: "pokedex#view_pokemon_show", as: :view_pokemon_show
  get "questions", to: "questions#preg", as: :questionslist

  root 'welcome#comienza'

  resources :questions
  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
