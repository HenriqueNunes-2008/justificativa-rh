/**
 * Dashboard RH
 */

import { iniciarVisualizacao } from "./visualizar.js";
import { iniciarExclusao } from "./excluir.js";
import { iniciarPdf } from "./pdf.js";
import "./logout.js";

console.log("Dashboard RH carregado.");

iniciarVisualizacao();
iniciarExclusao();
iniciarPdf();