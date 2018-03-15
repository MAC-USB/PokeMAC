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

end
