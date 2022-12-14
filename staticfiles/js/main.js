const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStar = (len) => {
    const children = form.children

    for(let i =0; i<children.length; i++){
        if(i<= len){
            children[i].classList.add('checked')
        }
        else{
            children[i].classList.remove('checked')
        }
    }

}


const handleSelect = (selection) => {
  switch (selection) {
      case 'first':{
          handleStar(1)
          return
      }
      case 'second': {
          handleStar(2)
          return
      }
      case 'third': {
          handleStar(3)
          return
      }
      case 'fourth': {
          handleStar(4)
          return
      }
      case 'fifth': {
          handleStar(5)
          return
      }

  }
}
const getNumericValue = (stringValue) =>{

    let numericValue;

    if (stringValue === 'first') {
        numericValue = 1
    }
    else if (stringValue === 'second') {
        numericValue = 2
    }
    else if (stringValue === 'third') {
        numericValue = 3
    }
    else if (stringValue === 'fourth') {
        numericValue = 4
    }
    else if (stringValue === 'fifth') {
        numericValue = 5
    }
    else {
        numericValue = 0
    }
    return numericValue
}

if (one) {
    const arr = [one, two, three, four, five]

    arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
    }))

    arr.forEach(item=> item.addEventListener('click', (event)=>{
        // value of the rating not numeric
        const val = event.target.id

        let isSubmit = false
        form.addEventListener('submit', e=>{
            e.preventDefault()
            if (isSubmit) {
                return
            }
            isSubmit = true
            // course id
            const id = e.target.id
            // value of the rating translated into numeric
            const val_num = getNumericValue(val)

            $.ajax({
                type: 'POST',
                url: '/rate/',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'article_id': id,
                    'val': val_num,
                },
                success: function(response){
                    console.log(response)
                    confirmBox.innerHTML = `<h1>Successfully rated with ${response.score}</h1>`
                },
                error: function(error){
                    console.log(error)
                    confirmBox.innerHTML = '<h1>Ups... something went wrong</h1>'
                }
            })
        })
    }))
}