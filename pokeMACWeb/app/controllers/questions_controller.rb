class QuestionsController < ApplicationController
    layout 'app'
    def new
    end

    def index

        @questions = Question.all

        render layout: false
    end

    def preg
        if params[:title].eql? "huir"
            
        else
            redirect_to preg_path(Question.find_by(title:params[:title])) if params[:title]
        end
    end


    def create
        @question = Question.new(question_params)
        @question.save

        @user = User.find(current_user.id)
        @user.questions[@question.id] = true
        
        redirect_to @question

    end

    def show
        @map="kanto.jpg"
        @question = Question.find(params[:id])
    end


    private

    def question_params
        params.require(:question).permit(:title, :text)
    end

end
