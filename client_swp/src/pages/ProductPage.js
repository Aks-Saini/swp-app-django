// // src/ProductsPage.js

import React, { useEffect, useState } from "react";
import Papa from "papaparse";
import * as XLSX from "xlsx";
import CustomizedTables from "../components/productTable";
import ProductForm from "../components/productForm";
import VehicleModal from "../components/vehicleModal";
import productApi from "../utils/webApi/productApi";

const ProductsPage = () => {
  //   const [data, setData] = useState([]);

  //   useEffect(()=>{
  //     console.log(data);
  //   },[data]);

  //   const handleFileUpload = (event) => {
  //     const file = event.target.files[0];
  //     const fileReader = new FileReader();

  //     fileReader.onload = (e) => {
  //       const fileContent = e.target.result;
  //       if (file.type === 'text/csv') {
  //         // Parse CSV file
  //         Papa.parse(fileContent, {
  //           header: true,
  //           complete: (result) => {
  //             setData(result.data);
  //           },
  //         });
  //       } else if (file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') {
  //         // Parse Excel file
  //         const workbook = XLSX.read(fileContent, { type: 'binary' });
  //         const sheetName = workbook.SheetNames[0];
  //         const worksheet = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], { header: 1 });
  //         const headers = worksheet[0];
  //         const rows = worksheet.slice(1).map((row) =>
  //           headers.reduce((acc, header, index) => {
  //             acc[header] = row[index];
  //             return acc;
  //           }, {})
  //         );
  //         setData(rows);
  //       }
  //     };

  //     if (file.type === 'text/csv') {
  //       fileReader.readAsText(file);
  //     } else {
  //       fileReader.readAsBinaryString(file);
  //     }
  //   };
  const [productData, setProductData] = useState([]);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const fetchedProduct = await productApi.fetchProductData();
        console.log(fetchedProduct, "blablabla");
        setProductData(fetchedProduct);
      } catch (error) {
        console.error("Error fetching product data:", error);
      }
    };

    fetchProduct();
  }, []);

  const [vehicleModalOpen, setVehicleModalOpen] = useState(false);

  return (
    <div
      style={{ display: "flex", height: "calc(100vh - 92px)", padding: "10px" }}
    >
      <VehicleModal open={vehicleModalOpen} setOpen={setVehicleModalOpen} />
      <div style={{ width: "40%", height: "100%" }}>
        <ProductForm
          productData={productData}
          setProductData={setProductData}
          setVehicleModalOpen={setVehicleModalOpen}
        />
      </div>
      <CustomizedTables productData={productData} />
      {/* //       <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
//         <h1>Products</h1>
//         <input
//           type="file"
//           accept=".csv, .xlsx"
//           onChange={handleFileUpload}
//           style={{ display: 'none' }}
//           id="fileUpload"
//         />
//         <label htmlFor="fileUpload" style={{ cursor: 'pointer', padding: '10px', background: 'blue', color: 'white' }}>
//           Import CSV/Excel
//         </label>
//       </header>
//       <table>
//         <thead>
//           <tr>
//             {data.length > 0 && Object.keys(data[0]).map((key) => <th key={key}>{key}</th>)}
//           </tr>
//         </thead>
//         <tbody>
//           {data.map((row, index) => (
//             <tr key={index}>
//               {Object.values(row).map((value, idx) => (
//                 <td key={idx}>{value}</td>
//               ))}
//             </tr>
//           ))}
//         </tbody>
//       </table> */}
    </div>
  );
};

export default ProductsPage;
