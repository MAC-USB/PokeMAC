class QuestionsController < ApplicationController
    layout 'app'
    def new
    end

    def index

        @questions = Question.all

        render layout: false
    end

    def preg
        numero = params[:id]
        @huir = params[:title]
        if @huir.eql? "huir"
            redirect_to preg_path(Question.find(numero.to_i - 1))
        else
            @huir2 = false
            if Question.find_by(title:params[:title])
                if !numero == 0
                    @answer = Answer.new
                    @answer.question = Question.find(numero.to_i)
                    @answer.user = current_user
                    @answer.save
                end
                redirect_to preg_path(Question.find_by(title: params[:title]))
            else
                redirect_back(fallback_location: root_path)
            end
            
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
