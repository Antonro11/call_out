let localStream;
let remoteStream;
let localVideo = document.getElementById('localVideo');
let remoteVideo = document.getElementById('remoteVideo');

const constraints = {
  video: true,
  audio: true
};

const configuration = {
  'iceServers': [
    { 'urls': 'stun:stun.stunprotocol.org:3478' },
    { 'urls': 'stun:stun.l.google.com:19302' },
  ]
};

const peerConnection = new RTCPeerConnection(configuration);

navigator.mediaDevices.getUserMedia(constraints)
  .then(stream => {
    localStream = stream;
    localVideo.srcObject = localStream;
    localVideo.muted = true;
    stream.getTracks().forEach(track => peerConnection.addTrack(track, stream));
  })
  .catch(error => {
    console.error('Error accessing media devices.', error);
  });

peerConnection.addEventListener('track', event => {
  remoteStream = event.streams[0];
  remoteVideo.srcObject = remoteStream;
});

peerConnection.addEventListener('icecandidate', event => {
  if (event.candidate) {
    console.log('New ICE candidate:', event.candidate);
  }
});

peerConnection.createOffer()
  .then(offer => peerConnection.setLocalDescription(offer))
  .then(() => {
    // Send the offer to the remote peer using your signaling server
  })
  .catch(error => {
    console.error('Error creating offer.', error);
  });