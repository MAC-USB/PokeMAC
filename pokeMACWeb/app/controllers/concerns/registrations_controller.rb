class MembershipsController < Devise::RegistrationsController
  def new
  	devise :database_authenticatable, :authentication_keys => [:username]

  end 

  def edit
  end
  
end