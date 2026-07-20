import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./components/pages/Login";
import Dashboard from "./components/pages/Dashboard";
import Students from "./components/pages/Students";
import AddStudent from "./components/pages/AddStudent";
import EditStudent from "./components/pages/EditStudent";
import StudentDetails from "./components/pages/StudentDeatils";
import NotFound from "./components/pages/NotFound";
import Profile from "./components/pages/Profile";
import ProtectedRoute from "./routes/ProtectedRoute";
import DashboardLayout from "./Layouts/DashboardLayout";
import { AuthProvider } from "./context/AuthContext";

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<Login />} />

          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <DashboardLayout>
                  <Dashboard />
                </DashboardLayout>
              </ProtectedRoute>
            }
          />

          <Route
            path="/students"
            element={
              <ProtectedRoute>
                <DashboardLayout>
                  <Students />
                </DashboardLayout>
              </ProtectedRoute>
            }
          />

          <Route
            path="/students/add"
            element={
              <ProtectedRoute>
                <DashboardLayout>
                  <AddStudent />
                </DashboardLayout>
              </ProtectedRoute>
            }
          />

          <Route
            path="/students/:id/edit"
            element={
              <ProtectedRoute>
                <DashboardLayout>
                  <EditStudent />
                </DashboardLayout>
              </ProtectedRoute>
            }
          />

          <Route
            path="/students/:id"
            element={
              <ProtectedRoute>
                <DashboardLayout>
                  <StudentDetails />
                </DashboardLayout>
              </ProtectedRoute>
            }
          />

          <Route
            path="/profile"
            element={
              <ProtectedRoute>
                <DashboardLayout>
                  <Profile />
                </DashboardLayout>
              </ProtectedRoute>
            }
          />

          <Route path="*" element={<NotFound />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;