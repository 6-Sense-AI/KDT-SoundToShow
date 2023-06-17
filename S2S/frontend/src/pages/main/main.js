import React, { useEffect, useState } from 'react';
import './main.css'
import styled, { keyframes } from 'styled-components';
import axios from "axios";
// const fadeInAnimation = keyframes`
//   from {
//     opacity: 0;
//   }
//   to {
//     opacity: 1;
//   }
// `;

// const fadeInUp = keyframes`
//   0% {
//     opacity: 0;
//     transform: translate3d(0, 100%, 0);
// }
//   to {
//     opacity: 1;
//     transform: translateZ(0);
// }
// `;

// const MainTextContainer = styled.div`
//   opacity: 0;
//   animation: ${fadeInAnimation} 1s ease-in forwards;
// `;

// const AdditionalTextContainer = styled.div`
//   opacity: 0;
//   animation: ${fadeInUp} 1s ease-in 0.5s forwards;
  
// `;

// const Main = () => {
//   const [isVisible, setIsVisible] = useState(false);
//   const [isVisible2, setIsVisible2] = useState(false);
//   const [isVisible3, setIsVisible3] = useState(false);

//   useEffect(() => {
//     setTimeout(() => {
//         setIsVisible(true);
//       }, 1000);
//     setTimeout(() => {
//     setIsVisible2(true);
//       }, 1600);
//       setTimeout(() => {
//         setIsVisible3(true);
//           }, 900);
//   }, []);

//   return (
//     <div className='app'>
//       <MainTextContainer style={{ opacity: isVisible ? 1 : 0 }}>
//         <span className="main-text-01">S2S</span>
//         <span className="main-text-02">Sound to Show</span>
//       </MainTextContainer>
//       {isVisible && (
//       <AdditionalTextContainer>
//         <div>
//         <img
//               src="./img/music.png"
//               alt="music"
//               className="main-img-01"

//             />
//         </div> 
//       </AdditionalTextContainer>)}
//       {isVisible2 && (
//       <MainTextContainer>
//         <div>
//         <img
//               src="./img/music.png"
//               alt="music"
//               className="main-img-02"

//             />
//         </div> 
//       </MainTextContainer>)}
//       {isVisible3 && (
//       <AdditionalTextContainer>
//         <div>
//         <img
//               src="./img/music.png"
//               alt="music"
//               className="main-img-03"

//             />
//         </div> 
//       </AdditionalTextContainer>)}
//     </div>
//   );
// };
  
  //export default Main;

  function FileUpload() {
    const [selectedFile, setSelectedFile] = useState(null);
  
    const handleFileChange = (event) => {
      setSelectedFile(event.target.files[0]);
    };
  
    const handleUpload = () => {
      if (selectedFile) {
        // 파일 업로드 로직을 구현합니다.
        // 예를 들어, 서버로 파일을 전송하는 API를 호출하거나 다른 처리를 수행할 수 있습니다.
        console.log('업로드할 파일:', selectedFile);
      }
    };
  
    return (
      <div>
        <h2>파일 업로드</h2>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload}>업로드</button>
      </div>
    );
  }
  
  export default FileUpload;