class PokedexController < ApplicationController
    layout 'app'
    def quest
        @map="kanto.jpg"
        @question
        # @map1="https://s3-us-west-2.amazonaws.com/s.cdpn.io/200653/psykokwak.gif"
    end

    def pokemons

    end

    def pokelist
    	@pokemons = Pokemon.all

    	render layout: false
    end

    def preg
        redirect_to preg_path(Question.find_by(title:params[:title])) if params[:title]
    end

    def view_pokemon
        redirect_to view_pokemon_show_path(Pokemon.find_by(name:params[:name])) if params[:name]
    end

    def view_pokemon_show
        @pokemon = Pokemon.find_by(id:request.path_parameters[:id]) if request.path_parameters[:id]
    end
end
