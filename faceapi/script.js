const video = document.getElementById('video')

Promise.all([
    faceapi.nets.faceExpressionNet.loadFromUri('face-api.js//weights'),
    faceapi.nets.tinyFaceDetector.loadFromUri('face-api.js/weights'),
    faceapi.nets.faceLandmark68Net.loadFromUri('face-api.js/weights'),
    faceapi.nets.faceRecognitionNet.loadFromUri('face-api.js/weights')
]).then(startVideo) 

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}
startVideo()

const result = []
let start = Date.now()

video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas)
  const displaySize = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas, displaySize)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    result.push({'start' : start,
                'emotion': resizedDetections})
    console.log(result)
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
  }, 500)
  setInterval(async ()=> {
    
  })
})


