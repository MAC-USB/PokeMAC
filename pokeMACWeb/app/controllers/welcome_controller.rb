class WelcomeController < ApplicationController
  def index
  end

  def positions	
  	@users = User.all.order("created_at DESC")

  	render layout: false
  end

  def pokedex
  end

  def map
  end

  def challenges
  end
end
