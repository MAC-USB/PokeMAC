class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable

  def email_required?
    false
  end

  def email_changed?
    false
  end
  
  # use this instead of email_changed? for rails >= 5.1
  def will_save_change_to_email?
    false
  end
end
